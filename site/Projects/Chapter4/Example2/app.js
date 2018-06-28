

var main = function() {
	"use strict";

	$(".comment-input button").on("click", function(event){
		//console.log("Hello world!");
		//$(".comments").append("<p>this is a new comment</p>");
		//var $new_comment = $("<p>").text("this too is a new comment");
		var $new_comment = $("<p>").text($(".comment-input input").val())

		$(".comments").append($new_comment);
	});
	

};
 
$(document).ready(main);
