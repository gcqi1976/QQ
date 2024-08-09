open_update = True
open_use_old_result = True
source_file = "demo.txt"
final_file = "result.txt"
favorite_list = [
    "广东珠江",
    "CCTV-1",
    "CCTV-5",
    "CCTV-5+",
    "CCTV-13",
    "广东体育",
    "广东卫视",
    "大湾区卫视",
    "浙江卫视",
    "湖南卫视",
    "翡翠台",
]
    version=datetime.now().strftime("%Y%m%d-%H-%M-%S")+",url"
    successlist_tv = ["更新时间,#genre#"] +[version] + ['\n'] +\
                  ["whitelist,#genre#"] + remove_prefix_from_lines(successlist)
    successlist = ["更新时间,#genre#"] +[version] + ['\n'] +\
                  ["RespoTime,whitelist,#genre#"] + successlist
    blacklist = ["更新时间,#genre#"] +[version] + ['\n'] +\
                ["blacklist,#genre#"]  + blacklist
open_online_search = True
favorite_page_num = 5
default_page_num = 3
urls_limit = 15
open_keep_all = False
open_sort = True
response_time_weight = 0.5
resolution_weight = 0.5
recent_days = 30
ipv_type = "ipv4"
domain_blacklist = ["epg.pw"]
url_keywords_blacklist = []
open_subscribe = True
subscribe_urls = [
    "https://m3u.ibert.me/txt/fmml_dv6.txt",
    "https://m3u.ibert.me/txt/o_cn.txt",
    "https://m3u.ibert.me/txt/j_iptv.txt",
]
open_multicast = True
region_list = ["all"]
open_proxy = True
open_driver = False
open_use_old_result = True
