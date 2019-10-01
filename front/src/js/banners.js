
function Banners() {

};

Banners.prototype.run = function () {
    var self = this;
    self.listenAddBannerEvent();
    self.loadData();
};
Banners.prototype.createBannerItem = function(banner){
    var self = this;
    var tpl = template("banner-item",{"banner":banner});
    var bannerListGroup = $('.banner-list-group');
    var bannerItem = null;
    if(banner){
        bannerListGroup.append(tpl);
        bannerItem = bannerListGroup.find(".banner-item:last");
    }else{
        bannerListGroup.prepend(tpl);

        //添加轮播图内的信息
        bannerItem = bannerListGroup.find(".banner-item:first");
    }

                //添加图片
    self.addImageSelectEvent(bannerItem);
    self.addRemoveBannerEvent(bannerItem);
    self.addSaveBannerEvent(bannerItem);
}

Banners.prototype.loadData = function(){
    var self = this;
    xfzajax.get({
        'url':'/cms/banner_list/',
        'success':function (result) {
            var banners = result['data']
            for (var i=0;i<banners.length;i++){
                var banner = banners[i]
                self.createBannerItem(banner);

            }
        }
    })
};

//添加轮播图
Banners.prototype.listenAddBannerEvent = function(){
    var self = this;
    var addBanner = $('#add-banner-btn');
    addBanner.click(function () {
        var bannerListGroup = $('.banner-list-group');
        var length = bannerListGroup.children().length;
        if(length>=6) {
            window.messageBox.showInfo("最多只能添加6张轮播图")
            return;
        }else{
            self.createBannerItem();
        }

    })


}

//添加轮播图图片
Banners.prototype.addImageSelectEvent = function(bannerItem){
    var image = bannerItem.find('.thumbnail');
    var imageInput = bannerItem.find('.image-input');
    //文件不能打开文件选择框，只能通过input
    image.click(function () {
        imageInput.click()
    })
    imageInput.change(function () {
        var file = this.files[0];
        var formData = new FormData();
        formData.append("file",file)
        xfzajax.post({
            'url':'/cms/upload_file/',
            'data':formData,
            'processData':false,
            'contentType':false,
            'success':function (result) {
                if(result['code'] === 200){
                    var url = result['data']['url'];
                    image.attr('src',url)
                }
            }

        })

    })
}

//轮播图删除事件
Banners.prototype.addRemoveBannerEvent = function(bannerItem){
    var closeBtn = bannerItem.find('.close-btn');

    closeBtn.click(function () {
        var bannerId = bannerItem.attr('data-banner-id')
        if(bannerId){
            xfzalert.alertConfirm({
                'text':'您确定要删除轮播图吗？',
                'confirmCallback':function () {
                    xfzajax.post({
                        'url':'/cms/delete_banner/',
                        'data':{
                            'banner_id':bannerId
                        },
                        'success':function (result) {
                            if(result['code'] === 200){
                                bannerItem.remove();
                                window.messageBox.showSuccess('轮播图删除成功！')
                            }
                        }
                    })
                }
            })
        }else{
            bannerItem.remove()
        }
    });

}

//保存轮播图信息
Banners.prototype.addSaveBannerEvent = function(bannerItem){
    var saveBtn = $('.save-btn')
    var imageTag = bannerItem.find(".thumbnail")
    var priorityTag = bannerItem.find("input[name='priority']")
    var linkToTag = bannerItem.find("input[name='link_to']")
    var prioritySpan = bannerItem.find("span[class='priority']")
    var bannerId = bannerItem.attr("data-banner-id")
    if(bannerId){
        url = '/cms/edit_banner/'
    }else {
        url = '/cms/add_banner/'
    }
    saveBtn.click(function () {
        var image_url = imageTag.attr('src');
        var priority = priorityTag.val();
        var link_to = linkToTag.val();
        xfzajax.post({
            'url':url,
            'data':{
                'image_url':image_url,
                'priority':priority,
                'link_to':link_to,
                'pk':bannerId,
            },
            'success':function (result) {
                if(result['code'] === 200){
                    if(bannerId){
                        window.messageBox.showSuccess('轮播图修改成功！');
                    }else{
                        bannerId = result['data']['banner_id']
                        bannerItem.attr('data-banner-id',bannerId)
                        window.messageBox.showSuccess("轮播图添加完成！")
                    }
                    prioritySpan.text("优先级："+priority);
                }
            }
        })
    })
}


$(function () {
    var banners = new Banners();
    banners.run()
})