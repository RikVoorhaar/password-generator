# Password generator

This is a simple password generator, meant to generate passwords that one
can remember and type easily, without sacrificing on security. 

WARNING: This prints a new password in plaintext to your shell, so make sure
that your shell is secure, and that there are no malicious coworkers looking
over your shoulder.

- We use only common English words in camel case, making password easy to type
  and remember.
- No external dependencies
- We add a symbol or two inside the string of words
- Passwords are generated using a combination of a master password and a key,
  therefore this method is only as secure as the master password used.
- Password generation is consistent and stable, so passwords can always be
  re-generated in a version-independent manner. As such, they do not need to be
  stored. 
- We base the password on a list with 3695 common English words. Together with
  one random numeric and symbol character, this gives about 5e+16 possible
  passwords, which is therefore resistant to brute-force attacks.