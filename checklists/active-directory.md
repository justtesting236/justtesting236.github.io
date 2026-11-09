# Active Directory checklist

Generic checklist. Use it on authorized targets only.

## Enumeration
- [ ] Collect domain data for graph analysis
- [ ] List privileged groups and their members
- [ ] Review delegation (constrained, unconstrained, and resource-based)
- [ ] Find accounts with service principal names

## Credential hygiene
- [ ] Review password policy and fine-grained policies
- [ ] Check for accounts with passwords that never expire
- [ ] Review use of reversible encryption and legacy protocols

## Configuration
- [ ] Check SMB signing and LDAP signing
- [ ] Review certificate services configuration
- [ ] Confirm tiered administration boundaries

## Reporting
- [ ] Map each finding to the attack path it enables
- [ ] Provide remediation and a retest plan
