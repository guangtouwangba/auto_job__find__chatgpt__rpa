def is_satisfied_job(jobs) -> bool:
    """
    Filter jobs by strategies
    """
    strategies = [is_not_waibao, is_satisfy_three_years, is_not_exclude]
    return filter_strategies(jobs, strategies)


def filter_strategies(job_description, strategies) -> bool:
    """
    Filter jobs by strategies
    """
    return all(strategy(job_description) for strategy in strategies)


def is_not_waibao(job_description) -> bool:
    """
    判断是否是外包工作
    :param job_description:
    :return:
    """
    key_words = ["外包", "外包项目", "外包工作", "外包项目工作", "外包项目招聘", "外包工作招聘", "驻场", "IT咨询",
                 "软件服务供应商"]
    return not any(key_word in job_description for key_word in key_words)


def is_satisfy_three_years(job_description) -> bool:
    """
    判断是否满足三年经验
    :param job_description:
    :return:
    """
    key_words = ["三年", "3年", "三年以上", "3年以上"]
    return any(key_word in job_description for key_word in key_words)


def is_not_exclude(job_description) -> bool:
    """
    判断是否不是排除的工作
    :param job_description:
    :return:
    """
    key_words = ["滴滴", "百度", "字节跳动", "携程", "小红书", "腾讯"]
    return not any(key_word in job_description for key_word in key_words)
