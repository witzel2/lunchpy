#!/usr/bin/env python
import random, os, sys
print random.choice(sys.argv[1:] if len(sys.argv) > 1 else [x.strip() for x in open(os.path.join(os.getenv('HOME') or os.getenv('USERPROFILE'), '.lunchrc'))] if os.path.exists(os.path.join(os.getenv('HOME') or os.getenv('USERPROFILE'), '.lunchrc')) else ['Usage: {0} [option1, option2, ...]\nor add choices (one per line) to .lunchrc in your home directory'.format(sys.argv[0])])

