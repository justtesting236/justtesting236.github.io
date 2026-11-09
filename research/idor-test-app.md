# IDOR in a test e-commerce app

**Status:** lab-only (deliberately vulnerable test application)
**Vulnerability class:** Broken object-level authorization (OWASP API1:2023 / A01:2021)

## Summary
In a test e-commerce app I built on top of a training template, the order endpoint returned any user's order when given its ID. The server checked that the user was logged in, but never checked that the order belonged to them.

## Impact
An authenticated customer could read other customers' order history, including shipping addresses. In a real application, this would be a privacy breach and a compliance problem.

## Reproduction (lab only)
1. Log in as user A and record the ID of one of your orders.
2. Log in as user B and request the same order ID.
3. The server returns user A's order. The expected response is HTTP 403 or 404.

## Root cause
The handler loaded the order by ID and returned it without comparing `order.owner_id` to the current user.

## Fix
Scope the query to the current user, so ownership is enforced in the database lookup rather than as a separate check that can be forgotten:

```python
@app.get("/orders/<int:order_id>")
@login_required
def get_order(order_id):
    order = Order.query.filter_by(id=order_id, owner_id=current_user.id).first()
    if order is None:
        abort(404)  # don't reveal whether the order exists
    return jsonify(order.to_dict())
```

## Regression test

```python
def test_user_cannot_read_other_users_order(client, user_a_order_id, user_b_session):
    response = client.get(f"/orders/{user_a_order_id}", headers=user_b_session)
    assert response.status_code == 404
```

## Timeline
- Found during lab testing.
- Fixed in the test app, with the regression test added to the CI pipeline.
