// LeetCode 2669 - Count Artist Occurrences On Spotify Ranking List
// https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    artist,\n"
    "    COUNT(1) AS occurrences\n"
    "FROM Spotify\n"
    "GROUP BY artist\n"
    "ORDER BY occurrences DESC, artist\n";
