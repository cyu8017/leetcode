<?php
$folders = array_filter(array_map('trim', file('/workspace/.tmp_php4013/batch_19.txt')));
$fail = 0;
$pass = 0;
$skip = 0;
foreach ($folders as $folder) {
    $cfg = json_decode(file_get_contents("/workspace/$folder/tests/config.json"), true);
    $cases = json_decode(file_get_contents("/workspace/$folder/tests/cases.json"), true);
    $kind = $cfg['kind'] ?? 'algo';
    $method = $cfg['method'] ?? 'solve';
    $src = file_get_contents("/workspace/$folder/solution.php");
    if ($kind === 'design' || $method === 'solve') {
        if (preg_match('/function\s+(\w+)\s*\(/', $src, $m) && $kind !== 'design') {
            // find Solution method
            if (preg_match('/class Solution.*?function\s+(\w+)\s*\(/s', $src, $m2)) {
                $method = $m2[1];
            }
        } else if ($kind === 'design') {
            $skip++;
            echo "SKIP design $folder\n";
            continue;
        }
    }
    // isolate in subprocess to avoid class redeclare
    $cmd = 'php -d memory_limit=512M -r ' . escapeshellarg(
        '$folder=' . var_export($folder, true) . ';' .
        '$method=' . var_export($method, true) . ';' .
        'require "/workspace/$folder/solution.php";' .
        '$cfg=json_decode(file_get_contents("/workspace/$folder/tests/config.json"),true);' .
        '$data=json_decode(file_get_contents("/workspace/$folder/tests/cases.json"),true);' .
        '$order=$cfg["paramOrder"]??[];' .
        '$sol=new Solution();' .
        '$ok=0;$bad=0;$i=0;' .
        'foreach($data["cases"] as $c){$i++; $args=[]; foreach($order as $p) $args[]=$c["args"][$p];' .
        '$got=$sol->$method(...$args);' .
        '$exp=$c["expected"];' .
        'if($got===$exp || $got==$exp){$ok++;} else {$bad++; fwrite(STDERR,"FAIL $folder case $i expected ".json_encode($exp)." got ".json_encode($got)."\n");}}' .
        'echo "$folder $ok/".($ok+$bad)." method=$method\n";' .
        'exit($bad?1:0);'
    );
    passthru($cmd, $code);
    if ($code === 0) $pass++; else $fail++;
}
echo "summary pass_folders=$pass fail_folders=$fail skip=$skip\n";
exit($fail ? 1 : 0);
