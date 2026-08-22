// LeetCode 3050 - Pizza Toppings Cost Analysis
// https://leetcode.com/problems/pizza-toppings-cost-analysis/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT *, RANK() OVER (ORDER BY topping_name) AS rk\n"
    "        FROM Toppings\n"
    "    )\n"
    "SELECT\n"
    "    CONCAT(t1.topping_name, ',', t2.topping_name, ',', t3.topping_name) AS pizza,\n"
    "    t1.cost + t2.cost + t3.cost AS total_cost\n"
    "FROM\n"
    "    T AS t1\n"
    "    JOIN T AS t2 ON t1.rk < t2.rk\n"
    "    JOIN T AS t3 ON t2.rk < t3.rk\n"
    "ORDER BY 2 DESC, 1 ASC;\n";
