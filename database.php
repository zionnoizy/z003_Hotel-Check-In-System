<?php

echo '<p align=center>Welcome to our Hotel Database</p>';
echo '</br>';
    	// Get a connection for the database
    	require_once('mysqli_connect.php');

    	//echo 'Test debug';

    	// Create a query for the database
    	$query = "SELECT * FROM hotel";

    	// Get a response from the database by sending the connection and the query
    	$response = @mysqli_query($dbc, $query);

    	// If the query executed properly proceed
    	if($response){
            	echo '<table align="center" border="1"
            	cellspacing="5" cellpadding="8">
            	<tr><td align="left"><b>ID</b></td>
            	<td align="left"><b>Room Number</b></td>
            	<td align="left"><b>Name</b></td>
            	<td align="left"><b>Status</b></td></tr>';

    	// mysqli_fetch_array returns row of data until no further data is available
            	while($row = mysqli_fetch_array($response)){
                    	echo '<tr><td align="left">' .
                    	$row['tagID'] . '</td><td align="left">' .
                    	$row['room_num'] . '</td><td align="left">' .
                    	$row['name'] . '</td><td align="left">' .
                    	$row['status'] . '</td><td align="left">';
                    	echo '</tr>';
            	}
            	echo '</table>';
    	} else {
            	echo "Couldn't issue database query<br />";
            	echo mysqli_error($dbc);
    	}
    	// Close connection to the database
    	mysqli_close($dbc);
?>
