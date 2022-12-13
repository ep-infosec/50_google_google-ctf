<?php
// Copyright 2022 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


namespace App\Http\Middleware;

use Illuminate\Support\Facades\App;
use Closure;

class ContentLength
{
    public function handle($request, Closure $next)
    {
        $response = $next($request);
        
        if (App::environment('local')) {
            $len = mb_strlen($response->content());
            $response->header('Content-Length', $len);
        }

        return $response;
    }
}
