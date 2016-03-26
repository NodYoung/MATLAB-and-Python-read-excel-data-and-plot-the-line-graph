%���ļ����ڼ���ͼ��׷������ʵ������ٵ�֮������
%ע�����û��ת��Ϊʵ�ʵľ���
realdata = xlsread('realpoint.xlsx');
trackingdata = xlsread('trackingpoint.xlsx');
realdatax = realdata(:, 1);
realdatay = realdata(:, 2);
trackingdatax = trackingdata(:, 1);
trackingdatay = trackingdata(:, 2);
xerror = abs(trackingdatax - realdatax);
yerror = abs(trackingdatay - realdatay);
distanterror = sqrt(xerror.^2 + yerror.^2);
figure('numbertitle','off','name','The error of x direction','color','white');
plot(xerror);title('The error of x direction');xlabel('frames');ylabel('error��pixel��');
figure('numbertitle','off','name','The error of y direction','color','white');
plot(yerror);title('The error of y direction');xlabel('frames');ylabel('error��pixel��');
figure('numbertitle','off','name','The error of relative distance','color','white');
plot(distanterror);title('The error of relative distance');xlabel('frames');ylabel('error��pixel��');
