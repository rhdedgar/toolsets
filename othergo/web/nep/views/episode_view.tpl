<!DOCTYPE html>
{{template "header.tpl"}}
<body class="hero-unit">
    <div class="container">
        <div class="row">
            <div class="hero-text">
                <h1>{{.show }} Season {{.season}} Episode {{.episode}}</h1>
                <h2>Click to play</h2>
                <video width="320" height="240" controls>
                  <source src="/vid/{{.show}}_{{.season}}_{{.episode}}.mp4" type="video/mp4">
                Your browser does not support the video tag.
                </video>
                <p>placeholder text for vars</p>
            </div>
        </div>
    </div>
</body>
{{template "footer.tpl"}}
