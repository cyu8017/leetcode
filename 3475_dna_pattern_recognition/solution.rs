// LeetCode 3475 - DNA Pattern Recognition
// https:// leetcode.com/problems/dna-pattern-recognition/

const QUERY: &str = r#"
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
"#;
