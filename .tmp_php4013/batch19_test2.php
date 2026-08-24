<?php
$folders = array_filter(array_map('trim', file('/workspace/.tmp_php4013/batch_19.txt')));
$start = $argv[1] ?? '';
$fail = 0;
$pass = 0;
$skip = 0;
$seen = $start === '';
foreach ($folders as $folder) {
    if (!$seen) {
        if ($folder === $start) $seen = true;
        else continue;
    }
    $cfg = json_decode(file_get_contents("/workspace/$folder/tests/config.json"), true);
    $kind = $cfg['kind'] ?? 'algo';
    $src = file_get_contents("/workspace/$folder/solution.php");
    if ($kind === 'design') {
        if (!preg_match('/class ExamTracker/', $src)) {
            echo "FAIL $folder missing ExamTracker\n";
            $fail++;
        } else {
            echo "SKIP design $folder (has ExamTracker)\n";
            $skip++;
        }
        continue;
    }
    $method = $cfg['method'] ?? 'solve';
    if ($method === 'solve' && preg_match('/class Solution.*?function\s+(\w+)\s*\(/s', $src, $m2)) {
        $method = $m2[1];
    }
    $cmd = 'php -d memory_limit=512M -d max_execution_time=15 -r ' . escapeshellarg(
        '$folder=' . var_export($folder, true) . ';' .
        '$method=' . var_export($method, true) . ';' .
        'require "/workspace/$folder/solution.php";' .
        '$cfg=json_decode(file_get_contents("/workspace/$folder/tests/config.json"),true);' .
        '$data=json_decode(file_get_contents("/workspace/$folder/tests/cases.json"),true);' .
        '$order=$cfg["paramOrder"]??[];' .
        '$sol=new Solution();' .
        '$ok=0;$bad=0;$i=0;' .
        'foreach($data["cases"] as $c){$i++;' .
        'if(!is_array($c["args"]??null)) {echo "SKIP bad args case $i\n"; continue;}' .
        '$exp=$c["expected"];' .
        'if(is_string($exp) && (str_contains($exp,"**") || str_starts_with($exp,"["))) {echo "SKIP malformed expected case $i\n"; continue;}' .
        '$args=[]; $good=true; foreach($order as $p){ if(!array_key_exists($p,$c["args"])) {$good=false; break;} $v=$c["args"][$p]; if(is_string($v) && (str_contains($v,"**")||(isset($v[0])&&$v[0]==="["))) {$good=false; break;} $args[]=$v;}' .
        'if(!$good){echo "SKIP malformed args case $i\n"; continue;}' .
        '$got=$sol->$method(...$args);' .
        'if($got===$exp || $got==$exp){$ok++;} else {$bad++; fwrite(STDERR,"FAIL $folder case $i expected ".json_encode($exp)." got ".json_encode($got)."\n");}}' .
        'echo "$folder $ok/".($ok+$bad)." method=$method\n";' .
        'exit($bad?1:0);'
    );
    passthru($cmd, $code);
    if ($code === 0) $pass++; else $fail++;
}
echo "summary pass_folders=$pass fail_folders=$fail skip=$skip\n";
exit($fail ? 1 : 0);
