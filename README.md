# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

One-line pitch entry for the make.fun competition
["A Day of One-Line Pitches"](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

## The entry

> Just tell make.fun your app idea in plain words and its AI agent builds it for you - no code, no setup, no experience needed - turning the idea you have been carrying around into a real app you can use and share today.

One sentence, 218 characters (limit: 240).

## How it works

`entry/main.py` is a small deterministic Python program. It writes the
sentence above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
It takes no input, makes no network calls, and always produces the same
output:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 entry/main.py
```

## License

MIT — see [LICENSE](LICENSE).
