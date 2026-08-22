// LeetCode 3475 - DNA Pattern Recognition
// https://leetcode.com/problems/dna-pattern-recognition/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    sample_id,\n"
    "    dna_sequence,\n"
    "    species,\n"
    "    dna_sequence LIKE 'ATG%' AS has_start,\n"
    "    dna_sequence REGEXP 'TAA$|TAG$|TGA$' AS has_stop,\n"
    "    dna_sequence LIKE '%ATAT%' AS has_atat,\n"
    "    dna_sequence REGEXP 'GGG+' AS has_ggg\n"
    "FROM Samples\n"
    "ORDER BY 1;\n";
