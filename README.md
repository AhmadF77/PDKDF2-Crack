# PDKDF2-Crack

A dictionary-based cracker for **PBKDF2-HMAC-SHA256** hashes. Useful for password
audits and CTF challenges.

## Requirements

- Python 3

## Usage

```bash
python pdkdf2_crack.py -hash <hash_file> -wordlist <wordlist>
```

- `-hash` — file containing the target PBKDF2-HMAC-SHA256 hash
- `-wordlist` — wordlist to try (e.g. rockyou.txt)

## Disclaimer

Intended for **authorized password audits, research, and CTF use only**. Only
crack hashes you own or are explicitly authorized to test.
