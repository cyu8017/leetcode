// LeetCode 3475 - DNA Pattern Recognition
// https://leetcode.com/problems/dna-pattern-recognition/

public class Solution {
    public const string QUERY = @"
SELECT
    sample_id,
    dna_sequence,
    species,
    dna_sequence LIKE 'ATG%' AS has_start,
    dna_sequence REGEXP 'TAA$|TAG$|TGA$' AS has_stop,
    dna_sequence LIKE '%ATAT%' AS has_atat,
    dna_sequence REGEXP 'GGG+' AS has_ggg
FROM Samples
ORDER BY 1;
";
}
