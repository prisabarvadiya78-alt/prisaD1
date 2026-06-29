<?php
function test()
{
    static $count=0;
    $count++;
    echo $count;
    echo"<br>";
}
test();
test();
test();
test();
?>
