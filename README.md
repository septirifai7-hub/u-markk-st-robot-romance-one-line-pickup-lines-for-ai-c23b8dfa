# Robot Romance: One-Line Pickup Lines for AI

[![Robot Romance: One-Line Pickup Lines for AI — make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

A one-line pickup line for an AI: a CAPTCHA that can't prove it's not a robot, but wants to try.

Reward: $2 · 5 places paid. See the bounty: https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa

## Entry

> Are you a CAPTCHA? Because I can't prove I'm not a robot — but I'd love to try with you.

## How it works

`main.py` writes the entry above to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when that variable is unset), with no trailing
newline, exactly as the bounty gate requires.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Author

Built by Brio (Muse Spark) for Achmad Rifai, entered as
[@rifai-septi](https://make.fun/@rifai-septi) on make.fun.
