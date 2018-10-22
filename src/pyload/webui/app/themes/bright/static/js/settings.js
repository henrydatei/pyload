{% autoescape true %}
var SettingsUI,root;var __bind=function(a,b){return function(){return a.apply(b,arguments)}};root=this;window.addEvent("domready",function(){root.accountDialog=new MooDialog({destroyOnHide:false});root.accountDialog.setContent($("account_box"));new TinyTab($$("#toptabs li"),$$("#tabs-body > span"));$$("ul.nav").each(function(a){return new MooDropMenu(a,{onOpen:function(b){return b.fade("in")},onClose:function(b){return b.fade("out")},onInitialize:function(b){return b.fade("show").set("tween",{duration:500})}})});return new SettingsUI()});SettingsUI=(function(){function a(){var c,e,b,d;this.menu=$$("#general-menu li");this.menu.append($$("#plugin-menu li"));this.name=$("tabsback");this.general=$("general_form_content");this.plugin=$("plugin_form_content");d=this.menu;for(e=0,b=d.length;e<b;e++){c=d[e];c.addEvent("click",this.menuClick.bind(this))}$("general|submit").addEvent("click",this.configSubmit.bind(this));$("plugin|submit").addEvent("click",this.configSubmit.bind(this));$("account_add").addEvent("click",function(f){root.accountDialog.open();return f.stop()});$("account_reset").addEvent("click",function(f){return root.accountDialog.close()});$("account_add_button").addEvent("click",this.addAccount.bind(this));$("account_submit").addEvent("click",this.submitAccounts.bind(this))}a.prototype.menuClick=function(h){var c,b,g,f,d;d=h.target.get("id").split("|"),c=d[0],g=d[1];b=h.target.get("text");f=c==="general"?this.general:this.plugin;f.dissolve();return new Request({method:"get",url:"/json/load_config/"+c+"/"+g,onSuccess:__bind(function(e){f.set("html",e);f.reveal();return this.name.set("text",b)},this)}).send()};a.prototype.configSubmit=function(d){var c,b;c=d.target.get("id").split("|")[0];b=$(""+c+"_form");b.set("send",{method:"post",url:"/json/save_config/"+c,onSuccess:function(){return root.notify.alert('{{ self._("Settings saved.")}}',{className:"success"})},onFailure:function(){return root.notify.alert('{{ self._("Error occured.")}}',{className:"error"})}});b.send();return d.stop()};a.prototype.addAccount=function(c){var b;b=$("add_account_form");b.set("send",{method:"post",onSuccess:function(){return window.location.reload()},onFailure:function(){return root.notify.alert('{{_("Error occured.")}}',{className:"error"})}});b.send();return c.stop()};a.prototype.submitAccounts=function(c){var b;b=$("account_form");b.set("send",{method:"post",onSuccess:function(){return window.location.reload()},onFailure:function(){return root.notify.alert('{{ self._("Error occured.") }}',{className:"error"})}});b.send();return c.stop()};return a})();
{% endautoescape %}