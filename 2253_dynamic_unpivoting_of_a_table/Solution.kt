// LeetCode 2253 - Dynamic Unpivoting Of A Table
// https://leetcode.com/problems/dynamic-unpivoting-of-a-table/

class Solution {
    companion object {
        const val QUERY = "CREATE PROCEDURE UnpivotProducts()\n" +
            "BEGIN\n" +
            "    SET group_concat_max_len = 5000;\n" +
            "    WITH\n" +
            "        t AS (\n" +
            "            SELECT column_name\n" +
            "            FROM information_schema.columns\n" +
            "            WHERE\n" +
            "                table_schema = DATABASE()\n" +
            "                AND table_name = 'Products'\n" +
            "                AND column_name != 'product_id'\n" +
            "        )\n" +
            "    SELECT\n" +
            "        GROUP_CONCAT(\n" +
            "            'SELECT product_id, \\'',\n" +
            "            column_name,\n" +
            "            '\\' store, ',\n" +
            "            column_name,\n" +
            "            ' price FROM Products WHERE ',\n" +
            "            column_name,\n" +
            "            ' IS NOT NULL' SEPARATOR ' UNION '\n" +
            "        ) INTO @sql from t;\n" +
            "    PREPARE stmt FROM @sql;\n" +
            "    EXECUTE stmt;\n" +
            "    DEALLOCATE PREPARE stmt;\n" +
            "END"
    }
}
