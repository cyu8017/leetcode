// LeetCode 2669 - Count Artist Occurrences On Spotify Ranking List
// https:// leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/

object Solution {
  final val QUERY: String = """SELECT
    artist,
    COUNT(1) AS occurrences
FROM Spotify
GROUP BY artist
ORDER BY occurrences DESC, artist
"""
}
