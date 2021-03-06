<!doctype html>
<html lang="en" ng-app="BannedApp">
<head>
  <meta charset="utf-8">
  <title>My AngularJS App</title>
  <link rel="stylesheet" href="static/css/app.css"/>
</head>
<body>
  <ul class="menu" style="display:none">
    <li><a href="#/view1">view1</a></li>
    <li><a href="#/view2">view2</a></li>
  </ul>

  <div ng-view></div>

  <div>Angular seed app: v<span app-version></span></div>

  <!-- In production use:
  <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.0.6/angular.min.js"></script>
  -->
  <script src="static/lib/angular/angular.js"></script>
  <script src="static/js/app.js"></script>
  <script src="static/js/services.js"></script>
  <script src="static/js/controllers.js"></script>
  <script src="static/js/filters.js"></script>
  <script src="static/js/directives.js"></script>
</body>
</html>
