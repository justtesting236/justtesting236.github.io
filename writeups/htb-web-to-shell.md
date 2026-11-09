# HTB: web-to-shell chain

**Platform:** Hack The Box (retired machine, published after retirement)
**Category:** Web, Linux
**Tools:** Nmap, ffuf, Burp Suite Community

## Summary
This machine goes from a public web page to a shell on the box. The useful lesson was about process: my first pass focused on the login page and missed a directory that the application exposed.

## Approach

**Recon.** Nmap found SSH and HTTP. The web page was a simple landing page with a login form.

**What I missed first.** I spent too long on the login form, trying default credentials and basic injection checks, without success. I didn't enumerate directories until I had nothing else.

**What changed.** Directory fuzzing with ffuf found an undocumented path. That path led to a file upload feature, which I tested with harmless file types first to learn what the server accepted.

**Lesson.** Enumerate broadly before going deep on one input. A quick directory scan at the start would have saved most of the time I lost.

## What I'd do differently
- Run directory enumeration in parallel with the first manual look at the application.
- Write notes after each step, so I can see which assumptions I haven't tested.

I don't include flags or the full exploit chain here, in line with the platform's writeup rules.
