all: tp1 tp2 tp3 tp4

tp1:
	cd TP1/rapport; \
	pandoc main.md -o ../rapport.pdf --toc; \

tp2:
	cd TP2/rapport; \
	pandoc main.md -o ../rapport.pdf --toc;

tp3:
	cd TP3/rapport; \
	pandoc main.md -o ../rapport.pdf --toc;

tp4:
	cd TP4/rapport; \
	pandoc main.md -o ../rapport.pdf --toc;
