# coding:utf-8
import os
import sys
import datetime
import configparser
import logging

config_file_path = "/Users/zhuxuanyu/python_xuexi/pil_play/cfg.ini"
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart


def send_mail(content, conf):
    # 获取要发送的收件人邮箱
    to_list = conf.get('email', "mailto_list")
    to_list = eval(to_list)
    me = conf.get('email', "me")  # 从哪发
    mail_host = conf.get('email', "mail_host")  # 邮箱服务器
    mail_user = conf.get('email', "mail_user")  # 登录服务器的用户名
    mail_pass = conf.get('email', "mail_pass")  # 邮箱授权码
    msg = MIMEMultipart()  # 多用途互联网邮件扩展
    msg['Subject'] = "to_do_list"  # 邮件标题
    msg['From'] = me  # 从哪里发 发件地址
    msg['To'] = ';'.join(to_list)  # 发到哪里
    mail_body = MIMEText(content, _charset='utf-8')
    msg.attach(mail_body)
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)  # 初始化stmp_ssl 对象   465邮件服务器端口
        s.connect(mail_host)  # 连接stmp邮件服务器
        s.login(mail_user, mail_pass)  # 登陆smtp服务器 用qq号 和  授权码登陆
        s.sendmail(me, to_list, msg.as_string())  # 登陆成功  发送邮件
        s.close()  # 关闭smtp 连接
        return True, "发送成功"
    except Exception as e:
        return False, str(e)


def main():
    logging.basicConfig(filename='/Users/zhuxuanyu/python_xuexi/pil_play/send_notice_info.txt', level=logging.ERROR)
    logfile = '/Users/zhuxuanyu/python_xuexi/pil_play/send_notice_info.txt'
    fh = logging.FileHandler(logfile, mode='a+')
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger = logging.getLogger()
    logger.addHandler(fh)
    # 读取配置文件
    conf = configparser.ConfigParser()
    conf.read(config_file_path)
    try:
        # 最近需要做的事情
        to_do_list = conf.get("notice", "to_do_list")
        to_do_list = eval(to_do_list)
        now = datetime.datetime.now()
        now_h_m = datetime.datetime.strftime(now, '%H:%M')
        notice_content = to_do_list.get(now_h_m)
        if notice_content:
            # 发送邮件
            flag, send_ok = send_mail(notice_content, conf)
            if not flag:
                logging.error("邮件发送失败" + "" + send_ok)

    except Exception as e:
        logging.error(str(e))

    return "ok"


if __name__ == "__main__":
    main()
