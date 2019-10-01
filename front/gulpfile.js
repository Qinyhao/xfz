const {parallel,series,src,dest,watch} = require('gulp')
const cssnano = require('gulp-cssnano')
const rename = require("gulp-rename")
const uglify = require("gulp-uglify")
const concat = require("gulp-concat")
const bs = require('browser-sync').create()
const sass = require("gulp-sass")
const util = require('gulp-util')
const sourcempas = require('gulp-sourcemaps')


//文件路径
var path = {
    'css':'./src/css/**/',
    'js':'./src/js/',
    'images':'./src/images/',
    'css_dist':'./dist/css/',
    'js_dist':'./dist/js/',
    'images_dist':'./dist/images/',
    'html':'./templates/**/'
}

//处理html文件任务
function html_task(){
    return src(path.html+'*.html')
        .pipe(bs.stream())
}

//css任务
function css_task(){
    return src(path.css+'*.scss')
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(dest(path.css_dist))
        .pipe(bs.stream())
}

//处理js任务
function js_task(){
    return src(path.js+'*.js')
        .pipe(sourcempas.init())
        .pipe(uglify().on("error",util.log))
        .pipe(rename({"suffix":".min"}))
        .pipe(sourcempas.write())
        .pipe(dest(path.js_dist))
        .pipe(bs.stream())
}

//监听修改任务
function watch_task(){
    watch(path.css+'*.scss',css_task);
    watch(path.js+'*.js',js_task);
    watch(path.html+'*.html',html_task);
}

//初始化browser-sync任务
function bs_task(){
    bs.init({
        'server':{
            'baseDir':'./'
        }
    })
}
exports.css_task = css_task;
exports.js_task = js_task;
exports.watch_task = watch_task;
exports.bs_task = bs_task;
exports.html_task = html_task;
// exports.default = parallel(bs_task,watch_task)

exports.default = series(watch_task)






