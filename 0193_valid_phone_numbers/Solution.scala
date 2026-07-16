object Solution {
  final val SCRIPT: String = """
#!/bin/bash
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
"""
}
