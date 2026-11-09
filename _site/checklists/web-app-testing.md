# Web application testing checklist

Generic checklist. Use it as a starting point, not a complete test plan.

## Recon
- [ ] Map the application, including hidden or undocumented paths
- [ ] Identify frameworks and third-party components
- [ ] Review client-side code for endpoints, keys, and comments

## Authentication and session
- [ ] Check password reset and account recovery flows
- [ ] Test session expiry and logout invalidation
- [ ] Review cookie flags (Secure, HttpOnly, SameSite)

## Authorization
- [ ] Test object-level access with two accounts (IDOR)
- [ ] Test function-level access for privileged actions

## Input handling
- [ ] Test injection points with safe, detectable payloads
- [ ] Review file upload type and size checks
- [ ] Check output encoding in reflected and stored content

## Reporting
- [ ] Record evidence for each finding, with sensitive data redacted
- [ ] Assign severity and give concrete remediation steps
