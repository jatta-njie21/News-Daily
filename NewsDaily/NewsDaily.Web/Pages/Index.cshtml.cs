using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using NewsDaily.Web.Models;
using NewsDaily.Web.Services;

namespace NewsDaily.Web.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        public IndexModel(ILogger<IndexModel> logger, JsonFileNewsService newsService)
        {
            _logger = logger;
            NewsService = newsService;
        }

        public JsonFileNewsService NewsService { get; }
        public IEnumerable<News> News { get; private set; }

        public void OnGet()
        {
            News = NewsService.GetNews();
        }
    }
}