//헤더 반응형 애니메이션
$('.menu-toggle').click(function() {
	$('.site-nav').toggleClass('site-nav--open', 500);
	$(this).toggleClass('open');
});
