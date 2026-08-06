<?php
class Solution {
    function entityParser($text) {
        $entities = ["&quot;" => '"', "&apos;" => "'", "&amp;" => "&", "&gt;" => ">", "&lt;" => "<", "&frasl;" => "/"];
        // Replace &amp; last so other entities aren't broken; process longer first except amp last
        $order = ["&quot;", "&apos;", "&gt;", "&lt;", "&frasl;", "&amp;"];
        foreach ($order as $encoded) {
            $text = str_replace($encoded, $entities[$encoded], $text);
        }
        return $text;
    }
}
