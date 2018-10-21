
/**
 * This script gets message on the fb messenger site and gets the sentiment of each message
 */

window.onload = function() {
	last_msg = 0;
    let slides = $('.thumbnail').toArray();
	var MutationObserver = window.MutationObserver;
	var list = document.querySelector('#thumbnailList');
  	var observer = new MutationObserver(function(mutations) {  
		mutations.forEach(function(mutation) {
			if (mutation.type === 'childList') {
				var list_values = [].slice.call(list.children)
					.map( function(node) { return $(node).find('img:first').attr('src');
				});
				const split = list_values[0].split('=');
				const eventPID = split[1].split('&')[0];
				const sessionPID = split[2].split('&')[0];
				const urls = [];
				for (let i = 0; i < list_values.length; i++) {
					const url = "https://d2y36twrtb17ty.cloudfront.net/sessions/" +
						sessionPID + '/' + eventPID + '_et/thumbs/slide' + (i + 1) + '.jpg';
						console.log(url);
					$.get("https://10.19.213.54:5000/upload/" + url, function(data, status){
						// console.log(data);
					});
				}
				// console.log(urls);
				// const vidLink = $("meta[name='twitter:player:stream']" ).attr('content').split('?')[0].split('/')[6].split('.')[0];
				// const url = "https://d2y36twrtb17ty.cloudfront.net/sessions/" +
				// 		sessionPID + '/' + vidLink + '-56cfab13-a724-40ea-b4c5-a951015131de.mp4';
				// console.log(url);
			}
    	});
	});
	observer.observe(list, {
	attributes: true, 
	childList: true, 
	characterData: true 
	});
};