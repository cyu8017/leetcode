// LeetCode 2252 - Dynamic Pivoting of a Table
// https://leetcode.com/problems/dynamic-pivoting-of-a-table/

const char* QUERY =
    "\n"
    "CREATE PROCEDURE PivotProducts()\n"
    "BEGIN\n"
    "	SET group_concat_max_len = 5000;\n"
    "    SELECT GROUP_CONCAT(DISTINCT 'MAX(CASE WHEN store = \\'',\n"
    "               store,\n"
    "               '\\' THEN price ELSE NULL END) AS ',\n"
    "               store\n"
    "               ORDER BY store) INTO @sql\n"
    "    FROM Products;\n"
    "    SET @sql =  CONCAT('SELECT product_id, ',\n"
    "                    @sql,\n"
    "                    ' FROM Products GROUP BY product_id');\n"
    "    PREPARE stmt FROM @sql;\n"
    "    EXECUTE stmt;\n"
    "    DEALLOCATE PREPARE stmt;\n"
    "END\n";
