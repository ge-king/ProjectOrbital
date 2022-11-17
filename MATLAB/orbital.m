clear()
initialx = 100;
initialy = 100;
initialxv = 5;
initialyv = 5;
initialxa = 5;
initialya = 50;
runtime = 1000;
object1 = zeros(runtime,6);
object1(1,:) = [initialx initialy initialxv initialyv initialxa initialya];
object1(:,5) = initialxa;
object1(:,6) = initialya;

for i = 2:runtime
    object1(i,3) = object1(i-1,3) + object1(i-1,5);
    object1(i,4) = object1(i-1,4) + object1(i-1,6);
    object1(i,1) = object1(i-1,1) + object1(i,3);
    object1(i,2) = object1(i-1,1) + object1(i,4);
end

comet([object1(:,1) object1(:,2)]);
