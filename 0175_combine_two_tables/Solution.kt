class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    Person.firstName,\n" +
            "    Person.lastName,\n" +
            "    Address.city,\n" +
            "    Address.state\n" +
            "FROM Person\n" +
            "LEFT JOIN Address\n" +
            "    ON Person.personId = Address.personId\n" +
            ""
    }
}
