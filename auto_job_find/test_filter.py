from auto_job_find.filter import is_satisfied_job

jd = """
    北京昌平区龙泽天空之城
上海静安区氪空间 
关于我们:
滴滴国际金融团队是滴滴国际化的重要一员。我们在拉美地区积极推进电子支付、信贷、信用卡、商户收单等多元化服务，致力于为海外当地用户提供更加便捷、优质的数字金融服务体验。
我们诚挚邀请真诚、 可靠、勇于挑战的您，和我们携手并肩，迎接国际竞争的浪潮。和滴滴国际金融团队一起，实现从0到1，从1到100的快速成长。
职位描述：
1、参与滴滴国际化金融体系的设计、开发工作；
2、解决开发过程中遇到的技术和业务难题；
3、深度参与业务规划，讨论并提出有建设性的意见；
4、积极跟其他团队沟通和配合，推动项目进展。
任职要求：
1.营销领域3年及以上经验，熟悉整个营销领域并在某个子领域有成功的产品技术实施经历，有金融业务的营销经验者优先
2.实际参与中大型营销系统的技术建设，具备大流量高并发场景实际研发能力
3.基础扎实，精通Golang编程，掌握goruntime原理，具备良好的系统设计能力，熟练掌握常用的分布式系统开发技能（MySQL、Redis、MQ、RPC等），了解其底层原理及应用场景
4.熟悉常用设计模式及开发实践，熟悉面向对象和数据结构
5.较好的质量意识，对线上bug零容忍，有在线系统debug及调优经验
6.做事靠谱彻底，有责任心和抗压能力，能锲而不舍地跟进疑难问题直到解决
7.英文交流能力为加分项
立即沟通
Received message: Location:
北京昌平区龙泽天空之城
上海静安区氪空间 
关于我们:
滴滴国际金融团队是滴滴国际化的重要一员。我们在拉美地区积极推进电子支付、信贷、信用卡、商户收单等多元化服务，致力于为海外当地用户提供更加便捷、优质的数字金融服务体验。
我们诚挚邀请真诚、 可靠、勇于挑战的您，和我们携手并肩，迎接国际竞争的浪潮。和滴滴国际金融团队一起，实现从0到1，从1到100的快速成长。
职位描述：
1、参与滴滴国际化金融体系的设计、开发工作；
2、解决开发过程中遇到的技术和业务难题；
3、深度参与业务规划，讨论并提出有建设性的意见；
4、积极跟其他团队沟通和配合，推动项目进展。
任职要求：
1.营销领域3年及以上经验，熟悉整个营销领域并在某个子领域有成功的产品技术实施经历，有金融业务的营销经验者优先
2.实际参与中大型营销系统的技术建设，具备大流量高并发场景实际研发能力
3.基础扎实，精通Golang编程，掌握goruntime原理，具备良好的系统设计能力，熟练掌握常用的分布式系统开发技能（MySQL、Redis、MQ、RPC等），了解其底层原理及应用场景
4.熟悉常用设计模式及开发实践，熟悉面向对象和数据结构
5.较好的质量意识，对线上bug零容忍，有在线系统debug及调优经验
6.做事靠谱彻底，有责任心和抗压能力，能锲而不舍地跟进疑难问题直到解决
7.英文交流能力为加分项
    """

def test_filter_jobs():

    res = is_satisfied_job(jd)
    assert res is False


def test_is_not_exclude():
    from auto_job_find.filter import is_not_exclude
    assert is_not_exclude(jd) is False
