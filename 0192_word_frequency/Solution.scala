object Solution {
  final val SCRIPT: String = """
#!/bin/bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
"""
}
