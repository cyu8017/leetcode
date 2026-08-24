// LeetCode 3368 - First Letter Capitalization
// https://leetcode.com/problems/first-letter-capitalization/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE\n" +
            "    capitalized_words AS (\n" +
            "        SELECT\n" +
            "            content_id,\n" +
            "            content_text,\n" +
            "            SUBSTRING_INDEX(content_text, ' ', 1) AS word,\n" +
            "            SUBSTRING(\n" +
            "                content_text,\n" +
            "                LENGTH(SUBSTRING_INDEX(content_text, ' ', 1)) + 2\n" +
            "            ) AS remaining_text,\n" +
            "            CONCAT(\n" +
            "                UPPER(LEFT(SUBSTRING_INDEX(content_text, ' ', 1), 1)),\n" +
            "                LOWER(SUBSTRING(SUBSTRING_INDEX(content_text, ' ', 1), 2))\n" +
            "            ) AS processed_word\n" +
            "        FROM user_content\n" +
            "        UNION ALL\n" +
            "        SELECT\n" +
            "            c.content_id,\n" +
            "            c.content_text,\n" +
            "            SUBSTRING_INDEX(c.remaining_text, ' ', 1),\n" +
            "            SUBSTRING(c.remaining_text, LENGTH(SUBSTRING_INDEX(c.remaining_text, ' ', 1)) + 2),\n" +
            "            CONCAT(\n" +
            "                c.processed_word,\n" +
            "                ' ',\n" +
            "                CONCAT(\n" +
            "                    UPPER(LEFT(SUBSTRING_INDEX(c.remaining_text, ' ', 1), 1)),\n" +
            "                    LOWER(SUBSTRING(SUBSTRING_INDEX(c.remaining_text, ' ', 1), 2))\n" +
            "                )\n" +
            "            )\n" +
            "        FROM capitalized_words c\n" +
            "        WHERE c.remaining_text != ''\n" +
            "    )\n" +
            "SELECT\n" +
            "    content_id,\n" +
            "    content_text AS original_text,\n" +
            "    MAX(processed_word) AS converted_text\n" +
            "FROM capitalized_words\n" +
            "GROUP BY 1, 2;"
    }
}
