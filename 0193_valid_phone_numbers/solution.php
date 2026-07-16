<?php

// LeetCode 0193 - Valid Phone Numbers
$SCRIPT = <<<'SCRIPT'
#!/bin/bash
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
SCRIPT;