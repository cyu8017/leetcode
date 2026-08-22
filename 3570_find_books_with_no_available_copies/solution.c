// LeetCode 3570 - Find Books with No Available Copies
// https://leetcode.com/problems/find-books-with-no-available-copies/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT book_id, COUNT(1) current_borrowers\n"
    "        FROM borrowing_records\n"
    "        WHERE return_date IS NULL\n"
    "        GROUP BY 1\n"
    "    )\n"
    "SELECT book_id, title, author, genre, publication_year, current_borrowers\n"
    "FROM\n"
    "    library_books\n"
    "    JOIN T USING (book_id)\n"
    "WHERE current_borrowers = total_copies\n"
    "ORDER BY 6 DESC, 2;\n";
