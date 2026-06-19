import json

# 内置站点资料
SITE_DATA = {
    "site_name": "乐鱼体育",
    "url": "https://officialm-leyu.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "综合体育"],
    "tags": ["体育", "电竞", "真人", "棋牌"],
    "description": "乐鱼体育是一家提供多元化体育赛事和娱乐服务的在线平台，涵盖足球、篮球、网球等主流项目，以及电竞、真人娱乐等模块。"
}

# 备用资料（用于展示更多结构）
ADDITIONAL_SITES = [
    {
        "name": "乐鱼体育 - 电竞频道",
        "url": "https://officialm-leyu.com.cn/esports",
        "tags": ["电竞", "LOL", "DOTA2"],
        "short_desc": "专注电竞赛事投注与直播，覆盖全球热门项目。"
    },
    {
        "name": "乐鱼体育 - 真人娱乐",
        "url": "https://officialm-leyu.com.cn/live",
        "tags": ["真人", "百家乐", "轮盘"],
        "short_desc": "真人荷官互动娱乐，高清流畅体验。"
    }
]


def format_site_summary(site: dict) -> str:
    """将单个站点资料格式化为结构化摘要字符串"""
    name = site.get("site_name", site.get("name", "未知站点"))
    url = site.get("url", "")
    keywords = site.get("keywords", [])
    tags = site.get("tags", [])
    desc = site.get("description", site.get("short_desc", ""))

    parts = []
    parts.append(f"站点名称：{name}")
    parts.append(f"访问地址：{url}")
    if keywords:
        parts.append(f"核心关键词：{'、'.join(keywords)}")
    if tags:
        parts.append(f"标签分类：{'、'.join(tags)}")
    if desc:
        parts.append(f"站点简介：{desc}")

    return "\n".join(parts)


def generate_main_summary() -> str:
    """生成主站点摘要（包含附加站点一览）"""
    lines = []
    lines.append("==================== 乐鱼体育站点摘要 ====================")
    lines.append("")
    lines.append("【主站点】")
    lines.append(format_site_summary(SITE_DATA))
    lines.append("")
    lines.append("【附属频道】")
    for i, sub in enumerate(ADDITIONAL_SITES, 1):
        lines.append(f"  [{i}]")
        lines.append("  " + format_site_summary(sub).replace("\n", "\n  "))
        lines.append("")
    lines.append("==========================================================")
    return "\n".join(lines)


def save_summary_to_file(filepath: str = "site_summary_output.txt") -> None:
    """将摘要写入文本文件"""
    content = generate_main_summary()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已保存至：{filepath}")


def display_summary() -> None:
    """在控制台打印结构化摘要"""
    print(generate_main_summary())


def get_summary_dict() -> dict:
    """返回摘要的字典表示，便于后续处理"""
    return {
        "main": {
            "name": SITE_DATA["site_name"],
            "url": SITE_DATA["url"],
            "keywords": SITE_DATA["keywords"],
            "tags": SITE_DATA["tags"],
            "description": SITE_DATA["description"]
        },
        "channels": [
            {
                "name": s["name"],
                "url": s["url"],
                "tags": s["tags"],
                "description": s["short_desc"]
            }
            for s in ADDITIONAL_SITES
        ]
    }


def export_json(filepath: str = "site_summary.json") -> None:
    """将摘要数据导出为JSON文件"""
    data = get_summary_dict()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"JSON已导出至：{filepath}")


if __name__ == "__main__":
    display_summary()
    print("\n---\n")
    save_summary_to_file()
    export_json()