
    var JSON = {
    	    menu: [
    	        {name: '0',link: '0', sub: [
    	            {name: 'lorem ipsum 0-0',link: '0-0', sub: null},
    	            {name: 'lorem ipsum 0-1',link: '0-1', sub: null},
    	            {name: 'lorem ipsum 0-2',link: '0-2', sub: null}
    	        ]
    	        },
    	        {name: '1',link: '1', sub: null},
    	        {name: '2',link: '2', sub: [
    	            {name: 'lorem ipsum 2-0',link: '2-0', sub: null},
    	            {name: 'lorem ipsum 2-1',link: '2-1', sub: null},
    	            {name: 'lorem ipsum 2-2',link: '2-2', sub: [
    	                {name: 'lorem ipsum 2-2-0',link: '2-2-0', sub: null},
    	                {name: 'lorem ipsum 2-2-1',link: '2-2-1', sub: null},
    	                {name: 'lorem ipsum 2-2-2',link: '2-2-2', sub: null},
    	                {name: 'lorem ipsum 2-2-3',link: '2-2-3', sub: null},
    	                {name: 'lorem ipsum 2-2-4',link: '2-2-4', sub: null},
    	                {name: 'lorem ipsum 2-2-5',link: '2-2-5', sub: null},
    	                {name: 'lorem ipsum 2-2-6',link: '2-2-6', sub: null}
    	            ]},
    	            {name: 'lorem ipsum 2-3',link: '2-3', sub: null},
    	            {name: 'lorem ipsum 2-4',link: '2-4', sub: null},
    	            {name: 'lorem ipsum 2-5',link: '2-5', sub: null}
    	        ]
    	        },
    	        {name: '3',link: '3', sub: null}
    	    ]
    	};

    	function makeDIV(elem,parent) {
    	    var html = [];
    	    html.push('<div class="collapse list-group-submenu" id="#' + parent + '"><div class="list-group panel">');
    	    $(elem).each(function() { html.push(makeA(this,parent)); });
    	    html.push('</div></div>');      
    	    return html.join("\n");
    	}

    	function makeA(elem,parent) {
    	    var html = [];
    	    if (elem.sub) {
    	        html.push('<a href="#' + elem.name + '" class="list-group-item collapsed" data-toggle="collapse" aria-expanded="true" data-parent="#' + parent + '">' + elem.name + '</a>');
    	        html.push(makeDIV(elem.sub,elem.name));
    	    } else {
    	        html.push('<a href="' + elem.link + '" class="list-group-item collapsed" data-toggle="collapse" aria-expanded="true" data-parent="#' + parent + '">' + elem.name + '</a>');
    	    }
    	    return html.join("\n");
    	}

    	$(".dropdown-menu li a").click(function(){
    	    var selText = $(this).text();
    	    $(this).parents('.btn-group').find('.dropdown-toggle').html(selText+' <span class="caret"></span>').dropdown('toggle');
    	    $("#Menu").html(makeDIV(JSON.menu,"Menu"));
    	  //location.reload(true);
    	})
    