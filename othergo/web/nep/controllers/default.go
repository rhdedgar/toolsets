package controllers

import (
	"github.com/astaxie/beego"
)

type MainController struct {
  beego.Controller
}

func (c *MainController) Get() {
  c.Data["Website"] = "shinobu.ninja"
  c.Data["Email"] = "shinobu@shinobu.ninja"
  c.TplName = "nep_recruit.tpl"
}

func (mdata *MainController) EpisodeView() {
  mdata.Data["show"] = mdata.Ctx.Input.Param(":show")
  mdata.Data["season"] = mdata.Ctx.Input.Param(":season")
  mdata.Data["episode"] = mdata.Ctx.Input.Param(":episode")
  mdata.TplName = "episode_view.tpl"
}
