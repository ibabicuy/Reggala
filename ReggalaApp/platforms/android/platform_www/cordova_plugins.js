cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "id": "de.fhg.fokus.famium.hbbtv.HbbTV",
        "file": "plugins/de.fhg.fokus.famium.hbbtv/www/HbbTV.js",
        "pluginId": "de.fhg.fokus.famium.hbbtv",
        "clobbers": [
            "hbbtv"
        ]
    },
    {
        "id": "cordova-plugin-x-toast.Toast",
        "file": "plugins/cordova-plugin-x-toast/www/Toast.js",
        "pluginId": "cordova-plugin-x-toast",
        "clobbers": [
            "window.plugins.toast"
        ]
    },
    {
        "id": "cordova-plugin-x-toast.tests",
        "file": "plugins/cordova-plugin-x-toast/test/tests.js",
        "pluginId": "cordova-plugin-x-toast"
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "cordova-plugin-whitelist": "1.3.2",
    "de.fhg.fokus.famium.hbbtv": "0.0.1",
    "cordova-plugin-x-toast": "2.6.0"
};
// BOTTOM OF METADATA
});