<?php

	error_reporting(E_ALL);
	ini_set('display_errors', '1');

	if(isset($_REQUEST['command'])) {
		$command = $_REQUEST['command'];	
	}
	
	if(isset($_REQUEST['device'])) {
		$device 	= $_REQUEST['device'];	
		$device 	= str_pad($device, 2, '0', STR_PAD_LEFT);
	}
	else {
		$device = null;
	}

	if(isset($_REQUEST['instruction'])) {
		$instruction = $_REQUEST['instruction'];	
	}
	else {
		$instruction = null;
	}
	
	$results = exec('echo "' . $command . ' ' . $device . ' ' . $instruction .'" | cec-client -s -d 1\n', $returnval);
	
	//echo 'echo "' . $command . ' ' . $device . ' ' . $instruction .'" | cec-client -s -d 1';
	
	print_r($returnval);
	
	//echo exec('ls -l\n') . "\n";
	
?>