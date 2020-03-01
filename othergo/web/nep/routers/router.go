package routers

import (
	"github.com/openshift/shinobu/controllers"
	"github.com/astaxie/beego"
)

func init() {
    beego.Router("/", &controllers.MainController{})
    beego.Router("/watch/?:show/:season([0-9]+)/:episode([0-9]+)", &controllers.MainController{}, "get:EpisodeView")
}
