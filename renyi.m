function [fitness]= renyi(Thresholds,hist)
    Thresholds=[Thresholds,0,255];
    Thresholds=sort(Thresholds);
    Total_Pixels = sum(hist);
    for i=1:256
        hist(i)=hist(i)/Total_Pixels;
    end
    alpha=0.5;
    H_alpha=[];
    for i=1:length(Thresholds)-1
       cumulative_class_sum=(sum(hist(Thresholds(i)+1:Thresholds(i + 1))))+eps ;
       H=0;
       for j=Thresholds(i)+1:Thresholds(i + 1)
           H=H+(hist(j)/cumulative_class_sum)^alpha;
       end
       H=(1/(1-alpha))*log(H+eps);
       H_alpha=[H_alpha,H];
    end
    fitness=sum(H_alpha);
    if (isinf(fitness))
        fitness=0;
    end
end
