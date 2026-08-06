# LeetCode 1410 - Html Entity Parser
# https://leetcode.com/problems/html-entity-parser/

def entity_parser(text)
  entities = { '&quot;' => '"', '&apos;' => "'", '&gt;' => '>', '&lt;' => '<', '&frasl;' => '/', '&amp;' => '&' }
  # amp last already ordered; do amp last
  entities.each { |encoded, decoded| text = text.gsub(encoded, decoded) }
  text
end
