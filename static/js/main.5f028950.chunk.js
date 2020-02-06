(this["webpackJsonputra-art-slam"]=this["webpackJsonputra-art-slam"]||[]).push([[0],{36:function(e,a,t){e.exports=t.p+"static/media/ra.62cc32a7.png"},37:function(e,a,t){e.exports=t.p+"static/media/slam_ico.9e5f8c16.svg"},41:function(e,a,t){e.exports=t(55)},46:function(e,a,t){},47:function(e,a,t){},55:function(e,a,t){"use strict";t.r(a);var n=t(0),l=t.n(n),o=t(22),r=t.n(o),i=(t(46),t(38)),c=t(10),m=(t(21),t(20)),s=t(18),d=t(19),u=t(30),p=t(27),g=t(23),h=t(17);var E=function(){return l.a.createElement("div",{style:{backgroundPosition:"50% 60%",backgroundSize:"cover",background:"#161616",width:"auto",height:"900px"}},l.a.createElement(u.a,{style:{borderRadius:0,backgroundPosition:"0% 2%",backgroundImage:"url(https://upload.wikimedia.org/wikipedia/commons/b/bd/Ouster_OS1-64_lidar_point_cloud_of_intersection_of_Folsom_and_Dore_St%2C_San_Francisco.png)",maxWidth:"100%",height:"350px"}},l.a.createElement("h1",{style:{color:"white"}},"What is SLAM and Navigation?"),l.a.createElement("p",{style:{color:"white",fontSize:"18px"}},l.a.createElement("b",null,"Simultaneous localization and mapping")," and ",l.a.createElement("b",null,"navigation")," refer to two independent but related processes:",l.a.createElement("ul",null,l.a.createElement("li",null,"constructing a map while keeping track of your location within it"),l.a.createElement("li",null,"finding an optimal path between your current location and a destination on that map"))),l.a.createElement("p",null,l.a.createElement(m.a,{href:"#tutorials-slam_and_nav",style:{marginTop:"20px",borderColor:"white",backgroundColor:"rgba(0, 0, 0, 0.4)"},variant:"primary"},"Learn more")),l.a.createElement("p",{style:{textAlign:"right"}},l.a.createElement("a",{style:{color:"white"},href:"https://commons.wikimedia.org/wiki/File:Ouster_OS1-64_lidar_point_cloud_of_intersection_of_Folsom_and_Dore_St,_San_Francisco.png",title:"via Wikimedia Commons"},"Daniel L. Lu")," ",l.a.createElement("a",{style:{color:"white"},href:"https://creativecommons.org/licenses/by/4.0"},"[CC BY 4.0]"))),l.a.createElement(g.a,{style:{width:"100%",margin:"0 0 0 0"}},l.a.createElement(h.a,{xs:3,style:{margin:"0 0 0 0",padding:"0 0 0 0"}},l.a.createElement(u.a,{style:{borderRadius:"0 10 0 10",backgroundPosition:"25% 2%",background:"black",maxWidth:"90%",height:"400px"}},l.a.createElement("p",{style:{color:"white",fontSize:"18px"}},"Featured Project"),l.a.createElement("h1",{style:{color:"white"}},"Caffeine"),l.a.createElement("p",{style:{color:"white",fontSize:"18px"}},"We are currently working on a robot, called Caffeine, for the 2020 IGVC competition."),l.a.createElement("p",null,l.a.createElement(m.a,{href:"https://github.com/UTRA-ART/SLAM",style:{marginTop:"20px",borderColor:"white",backgroundColor:"rgba(0, 0, 0, 0.4)"},variant:"primary"},"GitHub Repository")))),l.a.createElement(h.a,{style:{margin:"0 0 0 0",padding:"0 0 0 0"}},l.a.createElement(p.a,{style:{borderRadius:"10 0 10 0"}},l.a.createElement(p.a.Item,null,l.a.createElement("div",{style:{background:"black",width:"100%",height:"400px"}}),l.a.createElement(p.a.Caption,null,l.a.createElement("h1",null,"Meet the Team"),l.a.createElement("p",{style:{fontSize:"18px"}},"The SLAM and Navigation division of the Autonomous Rover Team is a small but dedicated group of students working towards creating fully autonomous robots.")))))))},b=(t(47),t(36)),y=t.n(b);var f=function(){return l.a.createElement("div",{style:{backgroundSize:"full",backgroundColor:"#f2f2f2",backgroundImage:"url("+y.a+")",width:"100%",minHeight:"655px"}},l.a.createElement("div",{style:{backgroundPosition:"2% 5%",width:"auto",height:"80px",backgroundImage:"url(https://upload.wikimedia.org/wikipedia/commons/b/bd/Ouster_OS1-64_lidar_point_cloud_of_intersection_of_Folsom_and_Dore_St%2C_San_Francisco.png)"}}),l.a.createElement(g.a,{style:{width:"100%",margin:"0 0 0 0"}},l.a.createElement(h.a,{xs:8,style:{margin:"0px 0px 0px 20px",padding:"0 0 0 0"}},l.a.createElement("div",{style:{margin:"25px 0px 0px 0px",padding:"0px 0px 20px 0px"}},l.a.createElement("div",{className:"scroll scroll4"},l.a.createElement("h2",{style:{margin:"10px 0 20px 0px",padding:"0 0 0 0 ",color:"#050505"}},"What is SLAM and Navigation?"),l.a.createElement("b",null,"Simultaneous localization and mapping")," and ",l.a.createElement("b",null,"navigation")," refer to two (mostly) independent but related processes:",l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("ul",null,l.a.createElement("li",null,"constructing a map while keeping track of your location within it"),l.a.createElement("li",null,"finding an optimal path between your current location and a destination on that map")),"Since these processes are independent (again mostly), we can focus on them in isolation.",l.a.createElement("h3",{style:{margin:"10px 0 20px 0px",padding:"0 0 0 0 ",color:"#050505"}},"Simultaenous Localization and Mapping"),l.a.createElement("p",{style:{color:"#050505"}},l.a.createElement("b",null,"Simultaenous localization and mapping"),", or SLAM, is really two problems in and of itself:",l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("ol",null,l.a.createElement("li",null,"Assuming we have an accurate map of the environment, we need a way to determine our relative location within it, i.e., ",l.a.createElement("b",null,"localization"),"."),l.a.createElement("li",null,"Assuming we can accuraely determine changes to our location, we need a way to build that map of the environment, i.e., ",l.a.createElement("b",null,"mapping"),".")),"Let's tackle these two problems seperately first."),l.a.createElement("h4",{style:{margin:"10px 0 20px 0px",padding:"0 0 0 0 ",color:"#050505"}},"Localization"),l.a.createElement("p",{style:{color:"#050505"}},"Suppose $x$ is our (unknown) location on the map. Typically, $x$ would be a vector in either $\\mathbb R ^2$ or $\\mathbb R^3$, depending on the dimensionality of the environment. Let's keep things simple and assume $x \\in \\mathbb R^2$.")))),l.a.createElement(h.a,{style:{margin:"0 0 0 0",padding:"0 0 0 0"}},l.a.createElement("div",{style:{margin:"25px 0px 0px 0px",padding:"0px 0px 20px 0px"}},l.a.createElement("div",{className:"scroll scroll4"})))))},w=t(37),x=t.n(w);var _=function(){return l.a.createElement("div",null,l.a.createElement(i.a,null,l.a.createElement(d.a,{bg:"light",expand:"lg"},l.a.createElement(d.a.Brand,{href:"#home"},l.a.createElement("img",{src:x.a,style:{width:40}})),l.a.createElement(d.a.Toggle,{"aria-controls":"basic-navbar-nav"}),l.a.createElement(d.a.Collapse,{id:"basic-navbar-nav"},l.a.createElement(s.a,{className:"mr-auto"},l.a.createElement(s.a.Link,{href:"#home"},"About"),l.a.createElement(s.a.Link,{href:"#tutorial"},"Tutorials"),l.a.createElement(s.a.Link,{href:"#doc"},"Documentation"))),l.a.createElement(m.a,{style:{borderColor:"white",backgroundColor:"rgba(0, 0, 0, 0.8)"},variant:"primary"},"Join us")),l.a.createElement(c.c,null,l.a.createElement(c.a,{path:"/tutorials-slam_and_nav"},l.a.createElement(f,null)),l.a.createElement(c.a,{path:"/home"},l.a.createElement(E,null)))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));r.a.render(l.a.createElement(_,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[41,1,2]]]);
//# sourceMappingURL=main.5f028950.chunk.js.map