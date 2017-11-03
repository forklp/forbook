$(document).scroll(function () {
    if ($(document).scrollTop() > 100) {
        $('.js-g-nav').addClass('g-nav-show');
    } else {
        $('.js-g-nav').removeClass('g-nav-show');
    }
});

$(function () {
    var search = $('.js-search1');
    search.focus(function () {
        search.addClass('focus-search-1');
    });
    search.blur(function () {
        search.removeClass('focus-search-1');
    });
});

$(function () {
    var lists = $('.m-li ul li');
    lists.hover(function () {
       $(this).addClass('s-underline');
    }, function () {
       $(this).removeClass('s-underline');
    });
    $('.m-li1 ul li').click(function () {
        $(this).addClass('s-bg1');
        var ind = $('.m-li1 ul li').index($(this));
        $('.m-li2').children('ul').eq(ind).show().siblings().hide();
        // $('.m-li2').children('ul').eq(ind).siblings().hide();
        $(this).siblings().removeClass('s-bg1');
    });
    $('.m-li2 ul li').click(function () {
        $(this).find('a').addClass('s-fc');
        $(this).siblings().find('a').removeClass('s-fc');
    })
});

$(function () {
    $('.js-box').hover(function () {
        $(this).find('.u-tit2').addClass('u-tit2hide').siblings('.u-ctHov').removeClass('u-ctHov-hide');
    }, function () {
        $(this).find('.u-tit2').removeClass('u-tit2hide').siblings('.u-ctHov').addClass('u-ctHov-hide');
    })
});

$(function () {
    $('.u-register').click(function() {
        $('.g-cover').show().find('.g-register').show().siblings('.g-login').hide();
    });
    $('.u-login').click(function() {
        $('.g-cover').show().find('.g-login').show().siblings('.g-register').hide();
    });
    $('.g-login, .g-register').click(function () {
        event.stopPropagation();
    });
    $('.g-cover').click(function () {
        $(this).hide();
    });
});

$(function () {
    $('.g-login .l-user').focus(function () {
        $(this).css({
            'background' : '#FFF',
            'z-index' : '2'
        }).siblings('.l-pwd').css({
            'background' : 'rgba(0,0,0,.0013)',
            'z-index' : '1'
        })
    });
    $('.g-login .l-pwd').focus(function () {
        $(this).css({
            'background' : '#FFF',
            'z-index' : '2'
        }).siblings('.l-user').css({
            'background' : 'rgba(0,0,0,.0013)',
            'z-index' : '1'
        })
    });

    $('.g-register .l-pwd').focus(function () {
        $(this).css({
            'background' : '#FFF',
            'z-index' : '2'
        }).siblings('.l-pwd2').css({
            'background' : 'rgba(0,0,0,.0013)',
            'z-index' : '1'
        })
    });
    $('.g-register .l-pwd2').focus(function () {
        $(this).css({
            'background' : '#FFF',
            'z-index' : '2'
        }).siblings('.l-pwd').css({
            'background' : 'rgba(0,0,0,.0013)',
            'z-index' : '1'
        })
    });
});

$(function () {
    $('.js-register').click(function () {
        $(this).parents('.g-login').hide().siblings('.g-register').show();
        event.preventDefault();
    });
    $('.js-login').click(function () {
        $(this).parents('.g-register').hide().siblings('.g-login').show();
        event.preventDefault();
    });
});

$(function () {
    $('.g-login .form-btn').click(function () {
        var username = $('#l-username').val();
        var password = $('#l-password').val();
        $.post('/bookstore/login/', {'account': username, 'password': password}, function (result) {
            alert(result);
        });
    });
});

$(function () {
    $('#r-username').change(function () {
        var reg=/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if(!reg.test($(this).val())) {
            $(this).next().html('请输入正确的邮箱地址！');
        } else {
            $(this).next().html('');
        }
    });
});

$(function () {
    $('#r-password2').change(function () {
        if($(this).val() !== $(this).siblings('#r-password').val()) {
            $(this).next().html('两次输入密码不一致！');
        } else {
            $(this).next().html('');
        }
    });
});

var email_flag = true;

$(function () {
    $('.g-register .code-btn').click(function () {
        var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        var email = $('#r-username').val();
        var pwd = $('#r-password2');
        if (! email_flag) {
            alert('验证码已发送！');
        }else if(!reg.test(email)) {
            alert('请输入正确的邮箱地址！');
        } else if ($('#r-password').val() === '') {
            alert('请输入密码！');
        } else if( pwd.val() !== pwd.siblings('#r-password').val() ) {
            alert('两次输入密码不一致！');
        } else {
            var username = $('#r-username').val();
            var password = $('#r-password').val();
            $.post('/bookstore/vercode/', {'account': username, 'password': password}, function (result) {
                email_flag = false;
                $('#code').removeAttr('disabled');
                $('.g-register .form-btn').removeAttr('disabled');
                alert('发送成功！');
            });
        }
    });
});

$(function () {
    $('#code').keyup(function () {
        var reg = /^\d{6}$/;
        if (reg.test($(this).val())) {
            $('.g-register .form-btn').removeClass('disable');
        }
    });
    $('.g-register .form-btn').click(function () {
        var username = $('#r-username').val();
        var password = $('#r-password').val();
        var code = $('#code').val();
        var reg = /^\d{6}$/;
        if (email_flag) {
            alert('请完成以上步骤！');
        } else if (! reg.test(code)) {
            alert('验证码格式错误！');
        } else {
            $.post('/bookstore/register/', {'account': username, 'password': password}, function (result) {
            });
            alert('注册成功！');
            $('.g-cover').hide();
        }
    });
});