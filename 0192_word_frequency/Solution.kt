class Solution {
    companion object {
        const val SCRIPT = """
#!/bin/bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
"""
    }
}
